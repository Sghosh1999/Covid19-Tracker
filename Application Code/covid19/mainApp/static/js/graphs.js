const allGraphs = document.querySelectorAll(".all-graphs .container");
const graphSelect = document.getElementById("graphSelect");
const gif = document.getElementById("gif");

function graphChoose() {
  const graph = graphSelect.value;
  // console.log(graph);

  // hide all graphs
  allGraphs.forEach((g) => {
    g.classList.add("hide1");
  });

  // Show the loader
  gif.classList.remove("hide1");

  // After 1.5 seconds display the graph
  setTimeout(() => {
    // hide the gif
    gif.classList.add("hide1");

    // display the appropiate graph
    allGraphs.forEach((g) => {
      if (g.classList.contains(graph)) {
        g.classList.remove("hide1");
      }
    });
  }, 1500);
}
