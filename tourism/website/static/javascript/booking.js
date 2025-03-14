document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("home").addEventListener("click",function(){
        window.location.href=this.getAttribute('data-url');
    });
    document.getElementById("discard").addEventListener("click",function(){
        window.location.href=this.getAttribute('data-url');
    });
    let quantityInput = document.getElementById("book-quantity");
    let parElement = document.getElementById("total-price");
    let price=document.getElementById("price");
    quantityInput.addEventListener("input", function () {
        let quantity = parseInt(this.value, 10) || 0;

        if (quantity <= 0) {
            this.value = 1; 
        } else {
            parElement.innerHTML=quantity*price.value
        }
    });
});