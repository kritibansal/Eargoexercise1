{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to our dollar store!\n",
      "Enter the price of the item : 83\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for -: 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-d08e8295ccaa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m'Welcome to our dollar store!'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprice\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter the price of the item : '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mrest\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m100\u001b[0m \u001b[1;33m-\u001b[0m \u001b[0mprice\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m'Returning'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'cents as '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mquarters\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrest\u001b[0m\u001b[1;33m/\u001b[0m\u001b[1;36m25\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "print ('Welcome to our dollar store!')\n",
    "price = input('Enter the price of the item : ')\n",
    "rest = 100 - price\n",
    "print ('Returning', rest, 'cents as ')\n",
    "quarters = rest/25\n",
    "rest = rest - 25*quarters\n",
    "dimes = rest/10\n",
    "rest = rest - 10*dimes\n",
    "nickles = rest/5\n",
    "rest = rest - 5*nickles\n",
    "pennies = rest\n",
    "print ('%d of quarter = %2d cents' % (quarters, quarters*25))\n",
    "print ('   %d of dime = %2d cents' % (dimes, dimes*10))\n",
    "print (' %d of nickle = %2d cents' % (nickles, nickles*5 ))\n",
    "print ('  %d of penny = %2d cents' % (pennies, pennies))\n",
    "test = 25*quarters + 10*dimes + 5*nickles + pennies\n",
    "print ('total change = %2d cents' % test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
