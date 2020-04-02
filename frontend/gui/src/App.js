import React, { Component } from "react";
import "./App.css";
import "antd/dist/antd.css";
import ArticleList from "./containers/ArticleList";

import CustomLayout from "./containers/Layout";

class App extends Component {
  state = {};
  render() {
    return (
      <CustomLayout>
        <ArticleList />
      </CustomLayout>
    );
  }
}

export default App;
