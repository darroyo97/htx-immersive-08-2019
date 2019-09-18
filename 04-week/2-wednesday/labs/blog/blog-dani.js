buildPage()

function buildPage() {
    var container = document.getElementById("container");
    container.appendChild(buildHeader());
}

function buildHeader() {
    var header = document.createElement("header");
    header.appendChild(buildTitle());
    return header;
}

function buildTitle() {
    var title = document.createElement("h1");
    title.textContent = "High on Coding";
    return title;
}