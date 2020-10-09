import React, { Component } from 'react';
 import { Editor } from '@tinymce/tinymce-react';
 import Typography from '@material-ui/core/Typography';
import PostsSubNav from './PostsSubNav.jsx';
import ResourceForm from './ResourceForm.jsx';

class AddResource extends Component {
   handleEditorChange = (content, editor) => {
     console.log('Content was updated:', content);
     alert('hey');
   }
  render() {
    return (
      <div>
        <Typography gutterBottom variant="h5" component="h2" align="center">
          What do you want to share?
        </Typography>
        <PostsSubNav current="add-resource" />
        <ResourceForm />
      </div>
    );
  }
}

export default AddResource;
