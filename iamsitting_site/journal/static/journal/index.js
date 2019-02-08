Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
    new Vue({
      el: '#starting',
      delimiters: ['${','}'],
      data: {
        articles: [],
        loading: true,
        currentArticle: {},
        message: null,
        newArticle: { 'article_title': null, 'article_body': null },
        search_term: '',
      },
      mounted: function() {
        this.getArticles();
      },
      methods: {
        getArticles: function() {
          let api_url = '/api/articles/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/articles/?search=${this.search_term}`
          }
          this.loading = true;
          this.$http.get(api_url)
              .then((response) => {
                this.articles = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        getArticle: function(id) {
          this.loading = true;
          this.$http.get(`/api/articles/${id}/`)
              .then((response) => {
                this.currentArticle = response.data;
                $("#editArticleModal").modal('show');
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        addArticle: function() {
          this.loading = true;
          this.$http.post('/api/articles/',this.newArticle)
              .then((response) => {
                this.loading = true;
                this.getArticles();
              })
              .catch((err) => {
                this.loading = true;
                console.log(err);
              })
        },
        updateArticle: function() {
          this.loading = true;
          this.$http.put(`/api/articles/${this.currentArticle.article_id}/`, this.currentArticle)
              .then((response) => {
                this.loading = false;
                this.currentArticle = response.data;
                this.getArticles();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        deleteArticle: function(id) {
          this.loading = true;
          this.$http.delete(`/api/articles/${id}/`)
              .then((response) => {
                this.loading = false;
                this.getArticles();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        }
      }
    });