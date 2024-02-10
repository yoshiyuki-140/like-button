
const scheme = "http://127.0.0.1:8000"
let objectId = 2
const endPoint = scheme + "/api/objects/" + objectId + "/";



async function getLikeCount() {
  let likeCount = await fetch(endPoint)
    .then(res => {
      if (res.ok) {
        return res.json()
      }
      throw new Error('指定のエンドポイントが無効です')
    })
    .then(data => data.like)
    .catch(e => {
      console.log(`問題発生:${e.message}`)
      throw e
    })
  return likeCount
}

let likeCount = getLikeCount()
console.log(likeCount)
