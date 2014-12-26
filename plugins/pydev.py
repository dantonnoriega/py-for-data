import sublime, sublime_plugin

# create column group
class PyColCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('set_layout', {
        	"cols": [0.0, 0.5, 1.0],
			"rows": [0.0, 1.0],
			"cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
		})
        self.window.run_command('run_existing_window_command', {
            "id": "repl_python_ipython",
            "file": "config/Python/Main.sublime-menu"
        })
        self.window.run_command('move_to_group', {"group": 1})

# create row group
class PyRowCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('set_layout', {
        	"cols":[0.0, 1.0],
        	"rows":[0.0, 0.5, 1.0],
        	"cells":[[0, 0, 1, 1], [0, 1, 1, 2]]
    	})
        self.window.run_command('run_existing_window_command', {
            "id": "repl_python_ipython",
            "file": "config/Python/Main.sublime-menu"
        })
        self.window.run_command('move_to_group', { "group": 1 })

class ReplViewAndExecuteCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('repl_transfer_current', {
            "scope": "lines",
            "action": "view_write"
        }) # send lines to REPL
        self.window.run_command('focus_group', {"group": 1}) # focus REPL
        self.window.run_command('repl_enter')
        self.window.run_command('focus_group', {"group": 0})
        self.window.run_command('move', {
            "by": "lines",
            "forward": True,
            "extend": False
            })

        # get the active view
        v = self.window.active_view()

        # we then take the line where the cursor is. if empty, keep hitting enter.
        while v.line(v.sel()[0]).empty():
            self.window.run_command('focus_group', {"group": 1}) # focus REPL
            self.window.run_command('repl_enter')
            self.window.run_command('focus_group', {"group": 0})
            self.window.run_command('move', {
                "by": "lines",
                "forward": True,
                "extend": False
                })


