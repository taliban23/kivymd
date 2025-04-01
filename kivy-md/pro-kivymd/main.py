from kivymd.uix.list import IconRightWidget
from kivy.uix.filechooser import error
from kivymd.uix.expansionpanel.expansionpanel import IconLeftWidget
from kivymd.uix.list import MDList
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from kivymd.toast.kivytoast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ThreeLineAvatarIconListItem
from helper import get_llm_response
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard

user_data=[]

class MD3Card(MDCard):
    """nothing special"""
class main(Screen):
    def trigger(self):

        if self.ids.user_value.text:
            invoke_string = f"""{self.ids.user_value.text}"""
            ai = get_llm_response(invoke_string)
            resp=self.ids.response
            resp.text=ai
            user_data.append(
                {
                    "question":invoke_string,
                    "response":resp.text
                }

            )
            self.ids.user_value.text=""
            print(user_data)
        else:
            exit()

    def menu(self):

      sheet_menu = MDGridBottomSheet()
      sheet_menu.add_item(
          icon_src="account",
          text='Account',
          callback= lambda x: toast("icon clicked")
      ),
      sheet_menu.add_item(
          icon_src="history",
          text='Chart History',

           callback= lambda x: self.to_Chart()

      ),
      sheet_menu.add_item(
          icon_src="theme-light-dark",
          text='Theme',#.format(app.theme_cls.theme_style),

          callback= lambda x:self.app.switch_theme_style()

      )
      sheet_menu.add_item(
          icon_src="cog",
          text='Settings',

          callback= lambda x: toast("icon clicked")

      )
      sheet_menu.add_item(
          icon_src="information",
          text='About',

          callback= lambda x: toast("icon clicked")

      )
      sheet_menu.add_item(
          icon_src="logout",
          text='Sign out',

          callback= lambda x: toast("icon clicked")

      )
      sheet_menu.open()


    def toast_masg(self):
        toast(text='clicked' )
    def to_Chart(self):
        self.manager.current="History"

class chart_history(Screen):
    def back(self):
        self.manager.current="main"
    def to_search(self):
        self.manager.current="Search_chart"

    def display_history(self):

        for items in user_data:
              box=self.ids.chart_box
              card=TwoLineAvatarIconListItem(

                           text=f"{items['question']}",
                           secondary_text=f"{items['response']}",
                           tertiary_text= "date"
                          )
              ico_right=IconRightWidget(
                  icon="delete"
              )
              card.add_widget(

                  ico_right
              )
              ico_left=IconRightWidget(
                  icon="text"
              )
              card.add_widget(
                  ico_left

              )

              box.add_widget(
                  card
              )

    def del_chart(self):
        pass
    # allow user to delete desired chart
    # allow user to search for a desired chart

class Sign_up(Screen):
    pass

class settings(Screen):
    # allow user to change theme
    # allow user to contact us
    pass
class Account(Screen):
    # allow user to delete account
    # allow user to view :[name,email]
    # sign out their account
    # allow user to clear chart
    pass
class Theme(Screen):
    # light dark
    # dark theme
    pass
class About(Screen):
    # a beach of code
    pass
class Search_chart(Screen):
      def search(self,query):
          search_box=self.ids.search_results
          search_box.clear_widgets()
          if query:
              for values in user_data:
                  if query.lower() in values['question'].lower() or query.lower() in values["response"]:
                       results=TwoLineAvatarIconListItem(
                           IconLeftWidget(
                               icon="text"
                           ),
                        #    IconRightWidget(
                        #     #    icon="delete",
                        #     #    icon_color='red',
                        #     #    on_release= lambda x,results=results:self.ids.search_results.remove_widget(results),
                        #     #    ),
                           text=f"{values['question']}",
                           secondary_text=f"{values['response']}",

                        #    self.screen.ids.md_list.remove_widget(instance)
                           #assaign my button to delete the select result
                          )
                       ico=IconRightWidget(
                             icon="delete",
                             on_release= lambda x,item=results:self.ids.search_results.remove_widget(item)

                       )
                       results.add_widget(ico)

                       search_box.add_widget(
                           results
                       )


class app(MDApp):
    def build(self):

       sm = ScreenManager()
       sm.add_widget(Sign_up(name="register"))
       sm.add_widget(main(name="main"))
       sm.add_widget(chart_history(name="History"))
       sm.add_widget(Search_chart(name="Search_chart"))
       self.theme_cls.theme_style_switch_animation = True
       self.theme_cls.primary_palette = "Indigo"
       self.theme_cls.theme_style = "Light"
       self.chart=chart_history()
       self.chart.display_history()
    #    self.theme_cls.primary_hue ="500"
       return  sm

if __name__ == "__main__":
    app().run()