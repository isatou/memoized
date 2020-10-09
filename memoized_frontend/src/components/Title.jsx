import React from 'react';
import { Editor } from '@tinymce/tinymce-react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
      width: '75ch',
    },
  },
}));

export default function Form() {
  const classes = useStyles();
  return (
    <form className={classes.root} noValidate autoComplete="off">
      <TextField id="standard-basic" label="Add a title for the resource" /><br />
      <TextField id="standard-tags" label="Add tags separated by commas" /><br />
    </form>
  );
}

