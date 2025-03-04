function togglePasswordVisibility() {
    const passwordInput = document.getElementById("reg-password");
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
async function hashit() {
    const passwordField = document.getElementById("reg-password");
    const password = passwordField.value;

    if (!password) return; // Do nothing if password is empty

    // Convert password to a SHA-256 hash
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, "0")).join("");

    passwordField.value = hashHex; // Replace password with hash
}

document.getElementById("reg-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default submission
    await hashit(); // Hash password
    this.submit(); // Submit form after hashing
});