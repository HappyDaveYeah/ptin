/**
 * Bootstrap
 *
 * An asynchronous boostrap function that runs before your Sails app gets lifted.
 * This gives you an opportunity to set up your data model, run jobs, or perform some special logic.
 *
 * For more information on bootstrapping your app, check out:
 * http://sailsjs.org/#documentation
 */

module.exports.bootstrap = function (cb) {

  // It's very important to trigger this callack method when you are finished 
  // with the bootstrap!  (otherwise your server will never lift, since it's waiting on the bootstrap)
    var dummyApps = [
    {
        "name": "Bus",
        "cat": "Traffic",
        "icon": "bus.png",
        "dir": "bus",
        "file_name": "bus.py"
    },
    {
        "name": "Lightning",
        "cat": "Energy",
        "icon": "lightning.png",
        "dir": "lightning",
        "file_name": "lightning.py"
    },
    {
        "name": "Cams",
        "cat": "Security",
        "icon": "cams.png",
        "dir": "cams",
        "file_name": "cams.py"
    },
    {
        "name": "Factory",
        "cat": "Productivity",
        "icon": "factory.png",
        "dir": "factory",
        "file_name": "factory.py"
    },
    {
        "name": "Health",
        "cat": "Security",
        "icon": "health.png",
        "dir": "health",
        "file_name": "health.py"
    },
    {
        "name": "Store",
        "cat": "Productivity",
        "icon": "store.png",
        "dir": "store",
        "file_name": "store.py"
    },
    {
        "name": "Lab",
        "cat": "Productivity",
        "icon": "lab.png",
        "dir": "lab",
        "file_name": "lab.py"
    }
];

    App.count().exec(function(err, count) {
        if(err) {
            sails.log.error('Already have data.');
            return cb(err);
        }
        if(count > 0) return cb();

        App.create(dummyApps).exec(cb);
    });

    cb();
};