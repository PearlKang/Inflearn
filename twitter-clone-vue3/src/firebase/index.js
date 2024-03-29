import firebase from "firebase";

const firebaseConfig = {
  apiKey: "AIzaSyDZeTsBp5RgIGj_rc7gMYGzc--YbTOC7ZQ",
  authDomain: "twitter-clone-inflearn-6f0eb.firebaseapp.com",
  projectId: "twitter-clone-inflearn-6f0eb",
  storageBucket: "twitter-clone-inflearn-6f0eb.appspot.com",
  messagingSenderId: "472643419182",
  appId: "1:472643419182:web:a4d74e788a80f514fdb3bf",
  measurementId: "G-7FRB0BNH5X",
};

firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const db = firebase.firestore();
export const storage = firebase.storage();

export const USER_COLLECTION = db.collection("users");
export const TWEET_COLLECTION = db.collection("tweets");
export const COMMENT_COLLECTION = db.collection("comments");
export const RETWEET_COLLECTION = db.collection("retweets");
export const LIKE_COLLECTION = db.collection("likes");
export const MESSAGE_COLLECTION = db.collection("messages");
