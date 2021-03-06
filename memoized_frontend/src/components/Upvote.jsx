import React from 'react';
import Badge from '@material-ui/core/Badge';
import { withStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import ThumbUpOutlined from '@material-ui/icons/ThumbUpOutlined';

const StyledBadge = withStyles((theme) => ({
  badge: {
    right: -3,
    //top: 13,
    border: `2px solid ${theme.palette.background.paper}`,
    padding: '0 4px',
  },
}))(Badge);

export default function Upvote(props) {
  return (
    <IconButton aria-label="cart">
      <StyledBadge badgeContent={props.count == 0 ? '0': props.count} color="secondary">
        <ThumbUpOutlined />
      </StyledBadge>
    </IconButton>
  );
}

