function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const eyeIcon = document.getElementById("show-pass");
    if (passwordInput && eyeIcon) {
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            eyeIcon.src = eyeClosedSrc; 
        } else {
            passwordInput.type = "password";
            eyeIcon.src = eyeOpenSrc; 
        }
    } else {
        console.warn("Required elements not found in the DOM");
    }
}
