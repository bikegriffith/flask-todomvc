var gulp = require('gulp');
var concat = require('gulp-concat');
var sass = require('gulp-ruby-sass');
var start = require('gulp-start-process');
var uglify = require('gulp-uglify');

var cfg = {
  jsRoot:  './flask_todomvc/static/js',
  cssRoot: './flask_todomvc/static/css',
};

gulp.task('jsminify', function() {
  gulp.src([
        // NOTE: Order matters here (e.g. Collections depend on Models being defined)
        cfg.jsRoot+'/models/*.js',
        cfg.jsRoot+'/collections/*.js',
        cfg.jsRoot+'/views/*.js',
        cfg.jsRoot+'/routers/*.js',
        cfg.jsRoot+'/app.js'
      ])
    .pipe(uglify())
    .pipe(concat("app.min.js"))
    .pipe(gulp.dest(cfg.jsRoot));
});

gulp.task('sassminify', function() {
  sass(cfg.cssRoot+'/', {style: "compressed"})
    .pipe(gulp.dest(cfg.cssRoot+'/'));
});

gulp.task('watch', function() {
  // Concatenate and compress javascript on any change
  gulp.watch([
      cfg.jsRoot+'/**/*.js',
      '!'+cfg.jsRoot+'/app.min.js' //<-- avoid infinite loop
    ], ['jsminify']);

  // Transpile SASS to CSS on any change
  gulp.watch([
      'flask_todomvc/static/css/**/*.scss'
    ], ['sassminify']);
});

gulp.task('flask-server', function(cb) {
  // Start Flask development server inside virtual environment
  start('. bin/activate && python server.py', cb);
});

gulp.task('default', ['watch', 'flask-server']);
