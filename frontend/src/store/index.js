import Vue from 'vue'
import Vuex from 'vuex'
import client from '@/api'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const state = {
  isLoggedIn: false,
}

const mutations = {
  loggedIn (state, token) {
    state.isLoggedIn = true
    client.defaults.headers.common['Authorization'] = `JWT ${token}`
    localStorage.setItem('token', token)
  },
  loggedOut (state) {
    state.isLoggedIn = false
    delete client.defaults.headers.common['Authorization']
    localStorage.clear()
  },
}

const actions = {
  login ({commit}, [username, password]) {
    return client.auth.login(username, password).then(res => {
      commit('loggedIn', res.data.token)
      return res
    })
  },
  logout ({commit}) {
    commit('loggedOut')
  },
  tryLoggedIn ({commit}) {
    const token = localStorage.getItem('token')
    if (token) {
      client.auth.verify(token).then(() => {
        commit('loggedIn', token)
      }, () => {
        // 不正なtoken
        localStorage.clear()
      })
<<<<<<< HEAD
=======
    }
    if (token) {
      commit('loggedIn', token)
>>>>>>> f66c4f5fbed62a269fbec28167f65f0b75b0c6a3
    }
  },
}

const getters = {
  isLoggedIn: state => state.isLoggedIn,
}

export default new Vuex.Store({
  strict: debug,
  actions,
  getters,
  mutations,
  state,
})
