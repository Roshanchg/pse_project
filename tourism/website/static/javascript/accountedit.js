document.getElementById("discard-button").addEventListener("click", function() {
    let confirmation=confirm("Do you want to Discard the changes? ")
    if (confirmation){
        alert("Discarded")
        window.location.href = this.getAttribute("data-url");
    }
    else{
        alert("Continue")
    }
});
document.getElementById("profile-edit").addEventListener("submit", async function(event) {
    event.preventDefault(); 
    let confirmation = confirm("Do you want to Confirm the changes?");

    if (confirmation) {
        alert("Changes Applied");
        this.submit(); 
    } else {
        alert("Continue Editing");
    }
});