document.getElementById('goto-login').addEventListener("click",function(){
    url=this.getAttribute('data-url');
    if(url){
        window.location.href=url;
    }
});
document.getElementById('book-now').addEventListener("click",function(){
    url=this.getAttribute('data-url');
    if(url){
        window.location.href=url;
    }
});
document.addEventListener("DOMContentLoaded", function () {
    let activeType = ""; // Stores the currently active filter type

    // Ensure the 'hot-button' is active on page load
    document.getElementById("hot-button").classList.add("active");

    document.querySelectorAll("#filters > button").forEach(button => {
        button.addEventListener("click", () => {
            // Remove 'active' class from all buttons
            document.querySelectorAll("#filters > button").forEach(btn => btn.classList.remove("active"));
            
            // Add 'active' class to the clicked button
            button.classList.add("active");

            // Update the active filter type
            activeType = button.getAttribute("data-type") || ""; // Get the data-type for the clicked button
            
            // Show the "Discover More" button again when a filter is selected
            document.getElementById("discover-more").style.display = "inline-block";
            // Check if none of the buttons is active, in which case 'hot-button' becomes active
            setHotButtonActive();
        });
    });

    // Function to check if no buttons are active, if true, activate 'hot-button'
    function setHotButtonActive() {
        const activeButtons = document.querySelectorAll("#filters > button.active");
        
        // If no button is active, add 'active' to hot-button
        if (activeButtons.length === 0) {
            document.getElementById("hot-button").classList.add("active");
        }
    }

    // When the "Discover More" button is clicked
    document.getElementById("discover-more").addEventListener("click", function (event) {
        event.preventDefault(); // Prevent default button behavior

        let baseUrl = this.getAttribute("data-url"); // Get the base URL
        let url = `${baseUrl}?all=True`; // Append 'all=True'
        if (activeType) {
            url += `&type=${activeType}`;
        }

        // Manually trigger HTMX request
        htmx.ajax('GET', url, {
            target: "#discover-contents-closed",
            swap: "innerHTML"
        });

        // Hide the "Discover More" button after it's clicked
        this.style.display = "none";

    });
});
