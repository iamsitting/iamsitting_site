import { RESET_POST_FORM } from './actions'

const reducer = (state, action) => {
  switch(action.type){
    case RESET_POST_FORM:
      return Object.assign({}, state, {
        postForm: {}
      })
    default:
      return state;
  }
}

export default reducer
