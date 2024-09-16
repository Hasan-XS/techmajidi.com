(() => {

  'use-strict'

  const themeSwiter = {

    init: function () {
      this.wrapper = document.getElementById('theme-switcher-wrapper')
      this.button = document.getElementById('theme-switcher-button')
      this.theme = this.wrapper.querySelectorAll('[data-theme]')
      this.themes = ['theme-orange', 'theme-purple', 'theme-green', 'theme-blue']
      this.events()
      this.start()
    },

    events: function () {
      this.button.addEventListener('click', this.displayed.bind(this), false)
      this.theme.forEach(theme => theme.addEventListener('click', this.themed.bind(this), false))
    },

    start: function () {
      let theme = this.themes[Math.floor(Math.random() * this.themes.length)]
      document.body.classList.add(theme)
    },

    displayed: function () {
      (this.wrapper.classList.contains('is-open'))
        ? this.wrapper.classList.remove('is-open')
        : this.wrapper.classList.add('is-open')
    },

    themed: function (e) {
      this.themes.forEach(theme => {
        if (document.body.classList.contains(theme))
          document.body.classList.remove(theme)
      })
      return document.body.classList.add(`theme-${e.currentTarget.dataset.theme}`)
    }

  }

  themeSwiter.init()

})()


// dark mode

const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

    // ذخیره مود انتخاب‌شده در localStorage
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
});

// بررسی ذخیره‌شده در localStorage
window.addEventListener('load', () => {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});