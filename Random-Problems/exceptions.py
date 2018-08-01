def main():
    num_dict= {0:2, 4:3, 34:23, 12:0, 89:0, 44:2, 9:0}

    for k,v in num_dict.items():
        try:
            print(k/v)
        except ZeroDivisionError as identifier:
            print(identifier, end=" ")
            print("Denominator: {} Numerator: {}".format(v,k))
            
if __name__ == '__main__':
    main()