// This is objec wiht method and 'this' keyword

const user = {
     name: 'naseem',
     lastName: 'khan',
     role: 'admin',
     loginCount: 56,
     facbookCountSignUp: true,
     coursList: [],
     buyCours: function (coursName) {
          this.coursList.push(coursName)
     },
     getCourseCount: function () {
          return `${this.name} is enroll total of ${this.coursList.length} course`
     },
     showUserDetails: function () {
          return `"${this.name}" last name "${this.lastName}" is enroll total of "${this.coursList.length}" course role is "${this.role}" is logincount "${this.loginCount}" facbookCountSignUp "${this.facbookCountSignUp}"`
     }
}

console.log(user.getCourseCount())
user.buyCours('new course')
console.log(user.getCourseCount())
console.log(user.showUserDetails())
