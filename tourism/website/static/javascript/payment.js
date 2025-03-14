document.getElementById('home').addEventListener("click",function(){
    window.location.href=this.getAttribute('data-url');
});
document.getElementById("payment").addEventListener("submit", async function(event) {
    event.preventDefault(); 
    let confirmation = confirm("Do you want to Confirm the Payment?");
    if (confirmation) {
        alert("Payment Done");
        this.submit(); 
    } else {
        alert("Payment Canceled");
    }
});