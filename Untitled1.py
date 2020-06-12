{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print('hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "x=3\n",
    "y=4\n",
    "z=x+y\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "reserved words cannot be \n",
    "used for the varaible names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H\n",
      "rogr\n"
     ]
    }
   ],
   "source": [
    "#string: \"\" ''\n",
    "str1='Hello Python'\n",
    "str2='programming '\n",
    "print(str1[0])\n",
    "print(str2[1:5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "programming programming programming \n"
     ]
    }
   ],
   "source": [
    "print(str2*3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "operators used:\n",
    "    +\n",
    "    *\n",
    "    [:]\n",
    "    in\n",
    "    not in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Python programming \n"
     ]
    }
   ],
   "source": [
    "str1='Hello Python '\n",
    "str2='programming '\n",
    "str3=str1+str2\n",
    "print(str3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apples', 'oranges']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "['apples','oranges']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "def\n"
     ]
    }
   ],
   "source": [
    "lst1=['abc','def','ghi', 1200]\n",
    "a=lst1[1]\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['physics', 'maths', 'newsub', 1900, 1200, 1300]\n"
     ]
    }
   ],
   "source": [
    "list=['physics','maths', 'newsub', 1900,1200,1300]\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['physics', 'maths', 1900, 1200, 1300]\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "del list[2]\n",
    "print(list)\n",
    "a=len(list)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "UsageError: %%writefile is a cell magic, but the cell body is empty.\n"
     ]
    }
   ],
   "source": [
    "%%writefile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-2-49cccaa16231>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-49cccaa16231>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    ipython nbconvert --to python *.ipynb\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "ipython nbconvert --to python *.ipynb"
   ]
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
