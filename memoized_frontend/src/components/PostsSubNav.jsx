import React from 'react';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    '& > *': {
      margin: theme.spacing(1),
    },
  },
}));

export default function PostsSubNav(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <ButtonGroup color="primary" aria-label="outlined primary button group">
        <Button component={Link} to="/add-how-to" variant={props.current == "how-to" ? "contained" : "outlined"}>How To</Button>
        <Button component={Link} to="/add-lesson-learnt" variant={props.current == "lesson-learnt" ? "contained" : "outlined"}>Lessons Learned</Button>
        <Button component={Link} to="/add-resource" variant={props.current == "add-resource" ? "contained" : "outlined"}>Resources</Button>
      </ButtonGroup>
    </div>
  );
}
