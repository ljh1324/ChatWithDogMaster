function addText(text) {
  // var ul = document.getElementById("chat-list");
  var ul = document.getElementsByClassName("chat-box")[0];
  var li = document.createElement("li");
  // var text = document.getElementById("chat-input").value;
  li.appendChild(document.createTextNode(text));
  // li.setAttribute("id", "element4"); // added line
  ul.appendChild(li);
  document.getElementById("chat-input").value = ''
}

