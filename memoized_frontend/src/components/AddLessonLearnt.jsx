import React, { Component } from 'react';
 import { Editor } from '@tinymce/tinymce-react';
 import Typography from '@material-ui/core/Typography';
import PostsSubNav from './PostsSubNav.jsx';
import TextAreaComponent from './TextAreaComponent.jsx';

class AddLessonLearnt extends Component {
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
        <PostsSubNav current="lesson-learnt" />
        <TextAreaComponent label="Share a lesson you learnt, good or bad that others can learn from. Add a title here." />
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
      <TextAreaComponent label="Add tags separated by commas" />
      </div>
    );
  }
}

export default AddLessonLearnt;
