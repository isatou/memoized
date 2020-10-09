import React, { Component } from 'react';
 import { Editor } from '@tinymce/tinymce-react';
 import Typography from '@material-ui/core/Typography';
import PostsSubNav from './PostsSubNav.jsx';
import TextAreaComponent from './TextAreaComponent.jsx';
import axios from 'axios';

class AddHowTo extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'content': '',
      'title': '',
      'tags': '',
    }
    this.handleTagsChange = this.handleTagsChange.bind(this);
    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.addPost = this.addPost.bind(this);
  }
   handleEditorChange = (content, editor) => {
     console.log('Content was updated:', content);
     this.setState({
       content: content,
     })
     alert('hey');
   }

  handleTitleChange(event) {
    this.setState({title: event.target.value});
  }

  handleTagsChange(event) {
    this.setState({tags: event.target.value});
  }

   addPost(data) {
    axios.post('localhost:8001/api/posts/', data)
      .then(response => {
        const posts = response.data;
        this.setState({ posts });
        console.log('here', posts);
      })
  }

  render() {
    return (
      <form onSubmit={this.addPost}>
        <Typography gutterBottom variant="h5" component="h2" align="center">
          What do you want to share?
        </Typography>
        <PostsSubNav current="how-to" />
        <TextAreaComponent label="What do you want to teach others how to do? Add a title here." onChange={this.handleTitleChange} />
      <Editor
        initialValue="<p>This is the initial content of the editor</p>"
        init={{
          height: 500,
          menubar: false,
          plugins: [
            'advlist autolink lists link image charmap print preview anchor',
            'searchreplace visualblocks code fullscreen',
            'insertdatetime media table paste code help wordcount'
          ],
          toolbar:
            'undo redo | formatselect | bold italic backcolor | \
            alignleft aligncenter alignright alignjustify | \
            bullist numlist outdent indent | removeformat | help'
        }}
        onEditorChange={this.handleEditorChange}
      />
      <TextAreaComponent label="Add tags separated by commas" onChange={this.handleTagsChange} />
      <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default AddHowTo;
