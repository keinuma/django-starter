import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const state = {
  isLoggedin: false,
}

const mutations = {
  loggedIn (state) {
    state.isLoggedin = true
  },
  loggedOut (state) {
    state.isLoggedin = false
  },
}

const actions = {
  login ({commit}) {
    commit('loggedIn')
  },
  logout ({commit}) {
    commit('loggedOut')
  },
}

const getters = {
  isLoggedin: state => state.isLoggedin,
}

export default new Vuex.Store({
  strict: debug,
  actions,
  getters,
  mutations,
  state,
})
