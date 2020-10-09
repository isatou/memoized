import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Upvote from './Upvote.jsx';
import Downvote from './Downvote.jsx';
import Chip from '@material-ui/core/Chip';

const useStyles = makeStyles({
  root: {
    maxWidth: 745,
  },
  media: {
    height: 140,
  },
});

export default function PostCard() {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea>
        {/*<CardMedia
          className={classes.media}
          image="/static/images/cards/contemplative-reptile.jpg"
          title="Contemplative Reptile"
        />*/}
        <CardContent>
           <div>
             <Chip size="small" label="How to" />
             <Chip size="small" label="Lessons Learnt" color="primary" />
             <Chip size="small" label="Resources" color="secondary" />
          <Typography variant="body" color="textSecondary" component="p" align="right" style={{bottom: 18, position: 'relative'}}>
            Shared by John Doe on January, 1, 2020.
          </Typography>
           </div>
          <Typography gutterBottom variant="h5" component="h2">
            Lizard
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging
            across all continents except Antarctica
          </Typography>
        </CardContent>
      </CardActionArea>
      {/*<CardActions>
        <Button size="small" color="primary">
          Bookmark
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>*/}
      <div>
            <Upvote />
            <Downvote />
      </div>
    </Card>
  );
}
