function emailSubs() {
  let objjj = document.getElementById("email_subscribe").value;
  document.emailSubs.action = "/subscribe/" + objjj;
  document.getElementById("email_subscribe").innerText =
    "Now Please Check Your Email for Confirmation";
}

function checkout() {
  console.log("Done")
}

function clearCart() {
  localStorage.clear();
  location.reload();
}

function coupon() {
  if (document.getElementById("coupon").value == "RuShX") {
    mystri = `<div class="row mb-3">
              <div class="col-md-6">
                <span class="text-black">Deduction</span>
              </div>
              <div class="col-md-6 text-right">
                <strong class="text-black">-Rs. ${totalPrice}</strong>
                </div>
            </div>`;
    document.getElementById("hacking").innerHTML = mystri;
    document.getElementById("totalPricee").innerText = 0;
  }
}
