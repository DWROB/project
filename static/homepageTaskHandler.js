document.addEventListener("DOMContentLoaded", function () {
  console.log("task handler loaded!");

  // task done - update db and turn the card green.

  // task delete - remove from db and dom

  doneBtns = document.querySelectorAll("#done");
  deleteBtns = document.querySelectorAll("#delete");

  doneBtns.forEach(function (doneBtn) {
    doneBtn.addEventListener("click", async function () {
      console.log(doneBtn.value);
    });
  });

  deleteBtns.forEach(function (deleteBtn) {
    deleteBtn.addEventListener("click", async function () {
      console.log(deleteBtn.value);
      const response = await fetch("/taskHandler" + input.value);
      console.log(response);
    });
  });
});
