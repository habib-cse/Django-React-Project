import React, { Component } from "react";
import Article from "../components/Article";
import axios from "axios";

class ArticleList extends Component {
  state = {
    articles: []
  };
  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/").then(result =>
      this.setState({
        articles: result.data
      })
    );
  }

  render() {
    return <Article data={this.state.articles} />;
  }
}

export default ArticleList;
