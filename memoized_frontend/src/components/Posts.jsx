import React, { Component } from 'react';
import PostCard from './PostCard.jsx';
import Typography from '@material-ui/core/Typography';
import axios from 'axios';

class Posts extends Component {
  constructor(props) {
    super(props);
    this.state = { posts: [] };
  }

  componentDidMount() {
    axios.get('http://localhost:8001/api/posts/')
      .then(response => {
        const posts = response.data;
        this.setState({ posts });
        console.log('here', posts);
      })
      .catch(function(error) {
        console.log('#######error', error);
      })
  }

  render() {
    return (
      <div>
        <Typography gutterBottom variant="h5" component="h2" align="center">
          Posts
        </Typography>
        {this.state.posts.map(post => <div><PostCard post={post}/><br /></div>)}
      </div>
    )
  }
}

export default Posts;