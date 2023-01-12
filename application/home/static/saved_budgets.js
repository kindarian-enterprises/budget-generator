// const APP_URL = process.env("APPURL");

const listObject = document.querySelector(".saved_budget_list");
window.addEventListener("load", function (e) {
  console.log("Page loaded!");
  fetch("http://127.0.0.1/budget/")
    .then((response) => response.json())
    .then((data) => {
      if (data.length == 0) {
        listObject.appendChild(`
        <ul>
        <li>Try adding your first budget to get started!</li>
        </ul>
    `);
      } else {
        data.forEach((budget) => {
          listObject.appendChild(`
        <ul>
        <li>Try adding your first budget to get started!</li>
        </ul>
    `);
        });
      }
      // data[0].length === 0;
    });
});
