(function () {
  var root = document.documentElement;
  var saved = localStorage.getItem("theme");
  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.setAttribute("data-theme", saved || (prefersDark ? "dark" : "light"));

  document.getElementById("theme-toggle").addEventListener("click", function () {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
  });

  var list = document.getElementById("research-list");
  fetch("research/manifest.json")
    .then(function (r) { return r.ok ? r.json() : []; })
    .then(function (items) {
      list.textContent = "";
      if (!items.length) {
        var empty = document.createElement("li");
        empty.textContent = "No reports yet. The first one arrives on Thursday.";
        list.appendChild(empty);
        return;
      }
      items.slice(0, 8).forEach(function (item) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = item.href;
        a.textContent = item.title;
        li.appendChild(a);
        list.appendChild(li);
      });
    })
    .catch(function () { list.innerHTML = "<li>Reports are not available yet.</li>"; });
})();
