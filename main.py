def print_star_digits():
    star_digits={
        '0': ['    *****  ',
              '  *       *', 
              '  *       *', 
              '  *       *', 
              '  *       *', 
              '  *       *', 
              '    *****  '], 
            
        '1': ['        *  ', 
              '     *  *  ', 
              '  *     *  ', 
              '        *  ', 
              '        *  ', 
              '        *  ',
              '        *  ', 
              '        *  '], 
        '2': ['    *  *   ', 
              '  *      * ',
              '  *       *',
              '   *     * ',
              '        *  ',
              '       *   ',
              '      *    ',
              '     *     ',
              '    *      ',
              '   *       ',
              '  * * * * *'],
        '3': ['    * * *   ',
              '  *       * ',
              '  *        *',
              '           *',
              '          * ',
              '    * * *   ',
              '          * ',
              '           *',
              '           *',
              ' *         *',
              '  *       * ',
              '    * * *   '],
        '4': ['   *       *',
              '   *       *',
              '   *       *',
              '   *       *',
              '   *       *',
              '   * * * * *',
              '           *',
              '           *',
              '           *',
              '           *',
              '           *'] }
    number=input ("Введите число (0,1,2,3 или 4): ")         
    if number in star_digits:
            for line in star_digits[number1]:
                    for i in line:
                        temp.append(st
    else:
            print("0,1,2,3 или 4.")
print_star_digits()
              
