const listObject = document.getElementById("saved-budgets-preview");

function displayRecentBudgets(budgets) {
  const { data } = budgets[0];
  const formated_budgets = [];
  data.forEach((budget) => {
    let [date, goal] = budget["_id"].split("--");
    date = format_date_string(date);

    formated_budgets.push([date, goal]);
  });
  if (data.length === 0) {
    listObject.innerHTML = `
    <ul>
    <li>No budgets to display!</li>
    </ul>
`;
  } else {
    const uListEl = document.createElement("ul");
    formated_budgets.forEach((budget) => {
      const listEl = this.document.createElement("li");

      const textNode1 = document.createTextNode(`Your Goal: ${budget[1]}   `);
      const textNode2 = this.document.createTextNode(
        `Date Created: ${budget[0]}`
      );

      listEl.classList.add(`preview-list-element`);
      listEl.appendChild(textNode1);
      listEl.appendChild(textNode2);
      uListEl.appendChild(listEl);
      listObject.appendChild(uListEl);
    });
  }
}

function format_date_string(input_date) {
  return input_date.slice(0, 9).replaceAll("-", "/");
}
