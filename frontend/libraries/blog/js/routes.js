import {BlogPost} from './models'

const routeHome = ['get', '#/',
  function(context){
    BlogPost.getPosts().then(function(data, context){
      $.each(data, function(i, item) {
        context.log(item.title, item.subtitle, item.author);
      });
    });
    // context.app.swap('');
    context.render('templates/home.hb', {}).appendTo(context.$element());
    //this.partial('../templates/home.template')
  }
];

const routeNewPost = ['get', '#/new-post',
  function(){
  }
]

const routeEditPost = ['get', '#/edit-post',
  function(){
  }
]

const routeViewPost = ['get', '#/view-post',
  function(){
  }
]

const routePostRequests = ['get', '#/post-requests',
  function(){
  }
]

const routeArchives = ['get', '#/archives',
  function(){

  }
]

const routeTemplates = ['get', 'templates/home.template',
  function(context){
    console.log(context);
  }
]

export const appRoutes = [
  routeHome,
  routeNewPost,
  routeEditPost,
  routeViewPost,
  routePostRequests,
  routeArchives,
  routeTemplates
]
