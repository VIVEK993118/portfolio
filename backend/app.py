import os
import re

import requests

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash

from dotenv import load_dotenv

from db import get_connection


load_dotenv()


app = Flask(__name__)

CORS(app)


MSG91_AUTHKEY = os.getenv("MSG91_AUTHKEY")
MSG91_TEMPLATE_ID = os.getenv("MSG91_TEMPLATE_ID")


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "success": True,
        "message": "Backend is running"
    })


@app.route("/request-otp", methods=["POST"])
def request_otp():

    try:

        data = request.get_json()

        name = data.get("name", "").strip()
        mobile = data.get("mobile", "").strip()
        password = data.get("password", "").strip()

        if not name:
            return jsonify({
                "success": False,
                "message": "Name is required"
            }), 400

        if not re.fullmatch(r"[6-9]\d{9}", mobile):

            return jsonify({
                "success": False,
                "message": "Enter a valid 10 digit Indian mobile number"
            }), 400

        if len(password) < 6:

            return jsonify({
                "success": False,
                "message": "Password must contain at least 6 characters"
            }), 400

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE mobile = %s",
            (mobile,)
        )

        existing_user = cursor.fetchone()

        cursor.close()
        connection.close()

        if existing_user:

            return jsonify({
                "success": False,
                "message": "This mobile number is already registered"
            }), 409

        url = "https://control.msg91.com/api/v5/otp"

        params = {
            "template_id": MSG91_TEMPLATE_ID,
            "mobile": "91" + mobile,
            "authkey": MSG91_AUTHKEY
        }

        response = requests.post(
            url,
            params=params,
            timeout=15
        )

        result = response.json()

        if response.ok and result.get("type") == "success":

            return jsonify({
                "success": True,
                "message": "OTP sent successfully"
            })

        return jsonify({
            "success": False,
            "message": "OTP could not be sent",
            "provider_response": result
        }), 500

    except Exception as error:

        print("REQUEST OTP ERROR:", error)

        return jsonify({
            "success": False,
            "message": "Server error while sending OTP"
        }), 500


@app.route("/verify-otp", methods=["POST"])
def verify_otp():

    try:

        data = request.get_json()

        name = data.get("name", "").strip()
        mobile = data.get("mobile", "").strip()
        password = data.get("password", "").strip()
        otp = data.get("otp", "").strip()

        if not name or not mobile or not password or not otp:

            return jsonify({
                "success": False,
                "message": "All fields are required"
            }), 400

        if not re.fullmatch(r"[6-9]\d{9}", mobile):

            return jsonify({
                "success": False,
                "message": "Invalid mobile number"
            }), 400

        if not re.fullmatch(r"\d{4,8}", otp):

            return jsonify({
                "success": False,
                "message": "Invalid OTP format"
            }), 400

        url = "https://control.msg91.com/api/v5/otp/verify"

        params = {
            "otp": otp,
            "mobile": "91" + mobile
        }

        headers = {
            "authkey": MSG91_AUTHKEY
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )

        result = response.json()

        if response.ok and "success" in str(
            result.get("message", "")
        ).lower():

            password_hash = generate_password_hash(password)

            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (name, mobile, password_hash)
                VALUES (%s, %s, %s)
                """,
                (
                    name,
                    mobile,
                    password_hash
                )
            )

            connection.commit()

            user_id = cursor.lastrowid

            cursor.close()
            connection.close()

            return jsonify({
                "success": True,
                "message": "Account created successfully",
                "user_id": user_id
            })

        return jsonify({
            "success": False,
            "message": "Invalid or expired OTP"
        }), 400

    except Exception as error:

        print("VERIFY OTP ERROR:", error)

        return jsonify({
            "success": False,
            "message": "Server error while verifying OTP"
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )