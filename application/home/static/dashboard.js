const listObject = document.getElementById("saved-budgets-preview");

function displayRecentBudgets(budgets) {
  if (budgets.length === 0) {
    listObject.innerHTML = `
      <ul>
      <li>No budgets to display!</li>
      </ul>
  `;
  } else {
    const uListEl = document.createElement("ul");
    budgets.forEach((budget) => {
      const listEl = this.document.createElement("li");

      const textNode1 = document.createTextNode(
        `Your Goal: ${budget["goal"]}   `
      );
      const textNode2 = this.document.createTextNode(
        `Date Created: ${budget["date"]}`
      );

      listEl.classList.add(`preview-list-element`);
      listEl.appendChild(textNode1);
      listEl.appendChild(textNode2);
      uListEl.appendChild(listEl);
      listObject.appendChild(uListEl);
    });
  }
}
