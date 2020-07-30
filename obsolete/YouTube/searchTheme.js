var fs = require('fs');

var google = require('googleapis'),
    youtubeV3 = google.youtube( { version: 'v3', auth: 'AIzaSyDW4Ch-zaHo6L8iQgKup2JX7TNuvA2aeuE' } );

var request =  youtubeV3.search.list({
    part: 'snippet',
    type: 'video',
    q: 'Bolsonaro',
    maxResults: 10,
    order: 'date',
    videoEmbeddable: true
}, (err,response) => {
  const newJson = JSON.stringify(response, null, '\t');
  //fs.writeFileSync('./data/output.json', newJson);
  const contentFromJson = JSON.parse(newJson)
  console.log(contentFromJson)
});