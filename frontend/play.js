document.getElementById('uploadImage').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const profilePic = document.getElementById('profilePic');
            profilePic.innerHTML = `<img src="${event.target.result}" alt="Profile">`;
        };
        reader.readAsDataURL(file);
    }
});