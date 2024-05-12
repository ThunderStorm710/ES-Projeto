import React from "react";

const Home = () => {
  document.documentElement.style.setProperty("--base", "var(--beige)");
  return (
    <div className="startpage">
      <h2>
        A crowd-sourced<br></br>quiz solving web app
      </h2>
    </div>
  );
};

export default Home;
