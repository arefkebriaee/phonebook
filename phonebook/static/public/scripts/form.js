function change_class() {
  form_name = document.querySelector("ul.form").firstElementChild;
  if (form_name.innerText == "Address:") {
    li = form_name.closest("li");
    li.style.height = "160px";
  }
}
function messages() {
  var message = document.querySelector("p.message");
  var div = document.querySelector("div.container");

  if (message) {
    message.style.display = "block";
    div.style.marginTop = "16px";
  }
}

messages();
change_class();
// setTimeout(change_class, 200);
