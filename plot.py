#!/usr/bin/env python
# -*-coding: utf8-*-
# Title: chessboard.py
# Author: Gribouillis
# Created: 2012-05-19 22:18:09.909216 (isoformat date)
# License: Public Domain
# Use this code freely.

version_info = (0, 1)
version = ".".join(map(str, version_info))

class Game(object):
    def __init__(self):
        self.pieces = u''.join(unichr(9812 + x) for x in range(12))
        self.pieces = u' ' + self.pieces[:6][::-1] + self.pieces[6:]
        self.allbox = u''.join(unichr(9472 + x) for x in range(200))
        self.box = [ self.allbox[i] for i in (2, 0, 12, 16, 20, 24, 44, 52, 28, 36, 60) ]
        (self.vbar, self.hbar, self.ul, self.ur, self.ll, 
         self.lr, self.nt, self.st, self.wt, self.et, self.plus) = self.box
        self.h3 = self.hbar * 3
        self.topline = self.ul + (self.h3 + self.nt) * 7 + self.h3 + self.ur
        self.midline = self.wt + (self.h3 + self.plus) * 7 + self.h3 + self.et
        self.botline = self.ll + (self.h3 + self.st) * 7 + self.h3 + self.lr
        self.tpl = u' {0} ' + self.vbar
 
        self.game = lambda squares: "\n".join(self.newBoard(squares))
        
    def newBoard(self,position):
        yield self.topline
        yield self.inter(*position[0])
        for row in position[1:]:
            yield self.midline
            yield self.inter(*row)
        yield self.botline

    def inter(self,*args):
        assert len(args) == 8
        return self.vbar + u''.join((self.tpl.format(self.pieces[a]) for a in args))


start_position = (
    [
        (-4, -2, -3, -5, -6, -3, -2, -4),
        (-1,) * 8,
    ] +
    [ (0,) * 8 ] * 4 +
    [
        (1,) * 8,
        (4, 2, 3, 5, 6, 3, 2, 4),
    ]
)


def main():
    """ Displaying menu after game has ended. """

    menu="""
    Thanks for playing the Chessmastah, would you like to go again?
    Type 'enter' to play again or 'exit' to quit.  >> """

    try:
        while True:
            g = Game()
            print g.game(start_position)
            choice=raw_input(menu)

            if choice == 'exit':
                print "\nAs you wish. Welcome back!"
                break

    except KeyboardInterrupt:
        sys.exit("\n\nOkok. Aborting.")



if __name__ == "__main__":
    main()
                            
