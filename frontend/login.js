const countries = [
    ["Afghanistan", "AF", "+93"],
    ["Albania", "AL", "+355"],
    ["Algeria", "DZ", "+213"],
    ["Andorra", "AD", "+376"],
    ["Angola", "AO", "+244"],
    ["Antigua and Barbuda", "AG", "+1"],
    ["Argentina", "AR", "+54"],
    ["Armenia", "AM", "+374"],
    ["Australia", "AU", "+61"],
    ["Austria", "AT", "+43"],
    ["Azerbaijan", "AZ", "+994"],
    ["Bahamas", "BS", "+1"],
    ["Bahrain", "BH", "+973"],
    ["Bangladesh", "BD", "+880"],
    ["Barbados", "BB", "+1"],
    ["Belarus", "BY", "+375"],
    ["Belgium", "BE", "+32"],
    ["Belize", "BZ", "+501"],
    ["Benin", "BJ", "+229"],
    ["Bhutan", "BT", "+975"],
    ["Bolivia", "BO", "+591"],
    ["Bosnia and Herzegovina", "BA", "+387"],
    ["Botswana", "BW", "+267"],
    ["Brazil", "BR", "+55"],
    ["Brunei", "BN", "+673"],
    ["Bulgaria", "BG", "+359"],
    ["Burkina Faso", "BF", "+226"],
    ["Burundi", "BI", "+257"],
    ["Cambodia", "KH", "+855"],
    ["Cameroon", "CM", "+237"],
    ["Canada", "CA", "+1"],
    ["Cape Verde", "CV", "+238"],
    ["Central African Republic", "CF", "+236"],
    ["Chad", "TD", "+235"],
    ["Chile", "CL", "+56"],
    ["China", "CN", "+86"],
    ["Colombia", "CO", "+57"],
    ["Comoros", "KM", "+269"],
    ["Congo", "CG", "+242"],
    ["Costa Rica", "CR", "+506"],
    ["Croatia", "HR", "+385"],
    ["Cuba", "CU", "+53"],
    ["Cyprus", "CY", "+357"],
    ["Czech Republic", "CZ", "+420"],
    ["Denmark", "DK", "+45"],
    ["Djibouti", "DJ", "+253"],
    ["Dominica", "DM", "+1"],
    ["Dominican Republic", "DO", "+1"],
    ["Ecuador", "EC", "+593"],
    ["Egypt", "EG", "+20"],
    ["El Salvador", "SV", "+503"],
    ["Equatorial Guinea", "GQ", "+240"],
    ["Eritrea", "ER", "+291"],
    ["Estonia", "EE", "+372"],
    ["Eswatini", "SZ", "+268"],
    ["Ethiopia", "ET", "+251"],
    ["Fiji", "FJ", "+679"],
    ["Finland", "FI", "+358"],
    ["France", "FR", "+33"],
    ["Gabon", "GA", "+241"],
    ["Gambia", "GM", "+220"],
    ["Georgia", "GE", "+995"],
    ["Germany", "DE", "+49"],
    ["Ghana", "GH", "+233"],
    ["Greece", "GR", "+30"],
    ["Grenada", "GD", "+1"],
    ["Guatemala", "GT", "+502"],
    ["Guinea", "GN", "+224"],
    ["Guinea-Bissau", "GW", "+245"],
    ["Guyana", "GY", "+592"],
    ["Haiti", "HT", "+509"],
    ["Honduras", "HN", "+504"],
    ["Hungary", "HU", "+36"],
    ["Iceland", "IS", "+354"],
    ["India", "IN", "+91"],
    ["Indonesia", "ID", "+62"],
    ["Iran", "IR", "+98"],
    ["Iraq", "IQ", "+964"],
    ["Ireland", "IE", "+353"],
    ["Israel", "IL", "+972"],
    ["Italy", "IT", "+39"],
    ["Jamaica", "JM", "+1"],
    ["Japan", "JP", "+81"],
    ["Jordan", "JO", "+962"],
    ["Kazakhstan", "KZ", "+7"],
    ["Kenya", "KE", "+254"],
    ["Kiribati", "KI", "+686"],
    ["Kuwait", "KW", "+965"],
    ["Kyrgyzstan", "KG", "+996"],
    ["Laos", "LA", "+856"],
    ["Latvia", "LV", "+371"],
    ["Lebanon", "LB", "+961"],
    ["Lesotho", "LS", "+266"],
    ["Liberia", "LR", "+231"],
    ["Libya", "LY", "+218"],
    ["Liechtenstein", "LI", "+423"],
    ["Lithuania", "LT", "+370"],
    ["Luxembourg", "LU", "+352"],
    ["Madagascar", "MG", "+261"],
    ["Malawi", "MW", "+265"],
    ["Malaysia", "MY", "+60"],
    ["Maldives", "MV", "+960"],
    ["Mali", "ML", "+223"],
    ["Malta", "MT", "+356"],
    ["Marshall Islands", "MH", "+692"],
    ["Mauritania", "MR", "+222"],
    ["Mauritius", "MU", "+230"],
    ["Mexico", "MX", "+52"],
    ["Micronesia", "FM", "+691"],
    ["Moldova", "MD", "+373"],
    ["Monaco", "MC", "+377"],
    ["Mongolia", "MN", "+976"],
    ["Montenegro", "ME", "+382"],
    ["Morocco", "MA", "+212"],
    ["Mozambique", "MZ", "+258"],
    ["Myanmar", "MM", "+95"],
    ["Namibia", "NA", "+264"],
    ["Nauru", "NR", "+674"],
    ["Nepal", "NP", "+977"],
    ["Netherlands", "NL", "+31"],
    ["New Zealand", "NZ", "+64"],
    ["Nicaragua", "NI", "+505"],
    ["Niger", "NE", "+227"],
    ["Nigeria", "NG", "+234"],
    ["North Korea", "KP", "+850"],
    ["North Macedonia", "MK", "+389"],
    ["Norway", "NO", "+47"],
    ["Oman", "OM", "+968"],
    ["Pakistan", "PK", "+92"],
    ["Palau", "PW", "+680"],
    ["Palestine", "PS", "+970"],
    ["Panama", "PA", "+507"],
    ["Papua New Guinea", "PG", "+675"],
    ["Paraguay", "PY", "+595"],
    ["Peru", "PE", "+51"],
    ["Philippines", "PH", "+63"],
    ["Poland", "PL", "+48"],
    ["Portugal", "PT", "+351"],
    ["Qatar", "QA", "+974"],
    ["Romania", "RO", "+40"],
    ["Russia", "RU", "+7"],
    ["Rwanda", "RW", "+250"],
    ["Saint Kitts and Nevis", "KN", "+1"],
    ["Saint Lucia", "LC", "+1"],
    ["Saint Vincent and the Grenadines", "VC", "+1"],
    ["Samoa", "WS", "+685"],
    ["San Marino", "SM", "+378"],
    ["Sao Tome and Principe", "ST", "+239"],
    ["Saudi Arabia", "SA", "+966"],
    ["Senegal", "SN", "+221"],
    ["Serbia", "RS", "+381"],
    ["Seychelles", "SC", "+248"],
    ["Sierra Leone", "SL", "+232"],
    ["Singapore", "SG", "+65"],
    ["Slovakia", "SK", "+421"],
    ["Slovenia", "SI", "+386"],
    ["Solomon Islands", "SB", "+677"],
    ["Somalia", "SO", "+252"],
    ["South Africa", "ZA", "+27"],
    ["South Korea", "KR", "+82"],
    ["South Sudan", "SS", "+211"],
    ["Spain", "ES", "+34"],
    ["Sri Lanka", "LK", "+94"],
    ["Sudan", "SD", "+249"],
    ["Suriname", "SR", "+597"],
    ["Sweden", "SE", "+46"],
    ["Switzerland", "CH", "+41"],
    ["Syria", "SY", "+963"],
    ["Taiwan", "TW", "+886"],
    ["Tajikistan", "TJ", "+992"],
    ["Tanzania", "TZ", "+255"],
    ["Thailand", "TH", "+66"],
    ["Timor-Leste", "TL", "+670"],
    ["Togo", "TG", "+228"],
    ["Tonga", "TO", "+676"],
    ["Trinidad and Tobago", "TT", "+1"],
    ["Tunisia", "TN", "+216"],
    ["Turkey", "TR", "+90"],
    ["Turkmenistan", "TM", "+993"],
    ["Tuvalu", "TV", "+688"],
    ["Uganda", "UG", "+256"],
    ["Ukraine", "UA", "+380"],
    ["United Arab Emirates", "AE", "+971"],
    ["United Kingdom", "GB", "+44"],
    ["United States", "US", "+1"],
    ["Uruguay", "UY", "+598"],
    ["Uzbekistan", "UZ", "+998"],
    ["Vanuatu", "VU", "+678"],
    ["Vatican City", "VA", "+39"],
    ["Venezuela", "VE", "+58"],
    ["Vietnam", "VN", "+84"],
    ["Yemen", "YE", "+967"],
    ["Zambia", "ZM", "+260"],
    ["Zimbabwe", "ZW", "+263"]
];


const countryPicker = document.getElementById("countryPicker");
const countrySelected = document.getElementById("countrySelected");
const countryFlag = document.getElementById("countryFlag");
const countryCodeText = document.getElementById("countryCodeText");
const countryList = document.getElementById("countryList");

const registeredCountryPicker =
    document.getElementById("registeredCountryPicker");

const registeredCountrySelected =
    document.getElementById("registeredCountrySelected");

const registeredCountryFlag =
    document.getElementById("registeredCountryFlag");

const registeredCountryCodeText =
    document.getElementById("registeredCountryCodeText");

const registeredCountryList =
    document.getElementById("registeredCountryList");

let selectedCountryCode = "+91";
let registeredSelectedCountryCode = "+91";


function getFlag(code) {
    return `https://flagcdn.com/w40/${code.toLowerCase()}.png`;
}


function createCountryList(listElement, flagElement, codeElement, isRegistered) {

    listElement.innerHTML = "";

    countries.forEach(function(country) {

        const option = document.createElement("button");

        option.type = "button";
        option.className = "country-option";

        const flag = document.createElement("img");

        flag.src = getFlag(country[1]);
        flag.alt = country[0];

        const text = document.createElement("span");

        text.textContent = `${country[0]} ${country[2]}`;

        option.appendChild(flag);
        option.appendChild(text);

        option.addEventListener("click", function(event) {

            event.stopPropagation();

            flagElement.src = getFlag(country[1]);
            codeElement.textContent = country[2];

            if (isRegistered) {
                registeredSelectedCountryCode = country[2];
            } else {
                selectedCountryCode = country[2];
            }

            listElement.classList.remove("show");

        });

        listElement.appendChild(option);

    });
}


createCountryList(
    countryList,
    countryFlag,
    countryCodeText,
    false
);

createCountryList(
    registeredCountryList,
    registeredCountryFlag,
    registeredCountryCodeText,
    true
);


countryFlag.src = getFlag("IN");
countryCodeText.textContent = "+91";

registeredCountryFlag.src = getFlag("IN");
registeredCountryCodeText.textContent = "+91";


countrySelected.addEventListener("click", function(event) {

    event.preventDefault();
    event.stopPropagation();

    registeredCountryList.classList.remove("show");

    countryList.classList.toggle("show");

});


registeredCountrySelected.addEventListener("click", function(event) {

    event.preventDefault();
    event.stopPropagation();

    countryList.classList.remove("show");

    registeredCountryList.classList.toggle("show");

});


countryList.addEventListener("click", function(event) {

    event.stopPropagation();

});


registeredCountryList.addEventListener("click", function(event) {

    event.stopPropagation();

});


document.addEventListener("click", function() {

    countryList.classList.remove("show");

    registeredCountryList.classList.remove("show");

});


const mobile = document.getElementById("mobile");

mobile.addEventListener("input", function() {

    this.value = this.value
        .replace(/\D/g, "")
        .slice(0, 10);

});


const registeredMobile =
    document.getElementById("registeredMobile");

registeredMobile.addEventListener("input", function() {

    this.value = this.value
        .replace(/\D/g, "")
        .slice(0, 10);

});


const loginForm =
    document.getElementById("loginForm");

const otpPopup =
    document.getElementById("otpPopup");

const otpInput =
    document.getElementById("otpInput");

const verifyOtp =
    document.getElementById("verifyOtp");

const closeOtp =
    document.getElementById("closeOtp");

const otpMessage =
    document.getElementById("otpMessage");


loginForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const mobileNumber = mobile.value.trim();

    if (mobileNumber.length !== 10) {

        alert("Please enter exactly 10 digits mobile number.");

        mobile.focus();

        return;

    }

    otpPopup.classList.add("show");

    otpInput.value = "";

    otpMessage.textContent =
        "OTP has been sent to your mobile number.";

});


verifyOtp.addEventListener("click", function() {

    const otp = otpInput.value.trim();

    if (otp.length !== 6) {

        otpMessage.textContent =
            "Please enter a valid 6 digit OTP.";

        return;

    }

    otpMessage.textContent =
        "OTP verified successfully!";

    setTimeout(function() {

        window.location.href = "game.html";

    }, 500);

});


closeOtp.addEventListener("click", function() {

    otpPopup.classList.remove("show");

});


const loginHere =
    document.getElementById("loginHere");

const registeredPopup =
    document.getElementById("registeredPopup");

const closeRegistered =
    document.getElementById("closeRegistered");

const registeredOtp =
    document.getElementById("registeredOtp");

const registeredMessage =
    document.getElementById("registeredMessage");


loginHere.addEventListener("click", function() {

    registeredPopup.classList.add("show");

    registeredMobile.value = "";

    registeredMessage.textContent = "";

});


closeRegistered.addEventListener("click", function() {

    registeredPopup.classList.remove("show");

});


const registeredOtpPopup =
    document.getElementById("registeredOtpPopup");

const registeredOtpInput =
    document.getElementById("registeredOtpInput");

const verifyRegisteredOtp =
    document.getElementById("verifyRegisteredOtp");

const closeRegisteredOtp =
    document.getElementById("closeRegisteredOtp");

const registeredOtpMessage =
    document.getElementById("registeredOtpMessage");


registeredOtp.addEventListener("click", function() {

    const mobileNumber =
        registeredMobile.value.trim();

    if (mobileNumber.length !== 10) {

        registeredMessage.textContent =
            "Please enter exactly 10 digits mobile number.";

        registeredMobile.focus();

        return;

    }

    registeredPopup.classList.remove("show");

    registeredOtpPopup.classList.add("show");

    registeredOtpInput.value = "";

    registeredOtpMessage.textContent =
        "OTP has been sent to your registered mobile.";

});


verifyRegisteredOtp.addEventListener("click", function() {

    const otp =
        registeredOtpInput.value.trim();

    if (otp.length !== 6) {

        registeredOtpMessage.textContent =
            "Please enter a valid 6 digit OTP.";

        return;

    }

    registeredOtpMessage.textContent =
        "OTP verified successfully!";

    setTimeout(function() {

        window.location.href = "game.html";

    }, 500);

});


closeRegisteredOtp.addEventListener("click", function() {

    registeredOtpPopup.classList.remove("show");

});
registeredOtpInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        event.preventDefault();
        verifyRegisteredOtp.click();
    }

});