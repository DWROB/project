// intended for draggable cards.  Not implemented initially.
document.addEventListener("DOMContentLoaded", function () {
  console.log("dom loaded");
  dragCard(document.getElementById("task-card"));
  console.log(dragCard);

  function dragCard(card) {
    var pos1 = 0,
      pos2 = 0,
      pos3 = 0,
      pos4 = 0;

    if (document.getElementById(card.id + "-drag")) {
      document.getElementById(card.id + "-drag").onmousedown = dragMouseDown;
    } else {
      card.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
      e = e || window.event;
      e.preventDefault();

      pos3 = e.clientX;
      pos4 = e.clientY;

      document.onmouseup = closeDragElement;

      document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
      e = e || window.event;
      e.preventDefault();

      pos1 = pos3 - e.clientX;
      pos2 = pos4 - e.clientY;
      pos3 = e.clientX;
      pos4 = e.clientY;

      card.style.top = card.offsetTop - pos2 + "px";
      card.style.left = card.offsetLeft - pos1 + "px";
    }

    function closeDragElement() {
      document.onmouseup = null;
      document.onmousemove = null;
    }
  }
});
