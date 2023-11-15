import { MongoClient } from 'mongodb';

/*
 * Requires the MongoDB Node.js Driver
 * https://mongodb.github.io/node-mongodb-native
 */

const agg = [
  {
    '$lookup': {
      'from': 'Montadoras', 
      'localField': 'Montadora', 
      'foreignField': 'Montadora', 
      'as': 'Montadoras'
    }
  }, {
    '$addFields': {
      'Pais': {
        '$first': '$Montadoras.País'
      }
    }
  }, {
    '$group': {
      '_id': '$Pais', 
      'Carros': {
        '$addToSet': '$Carro'
      }
    }
  }, {
    '$sort': {
      '_id': 1
    }
  }
];

const client = await MongoClient.connect(
  'mongodb://localhost:27017/'
);
const coll = client.db('Teste').collection('Carros');
const cursor = coll.aggregate(agg);
const result = await cursor.toArray();
await client.close();