class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []


        def backtrack(open_count,close_count, curr):
            if len(curr) == 2*n:
                ans.append("".join(curr))
                return

            for choice in ["(",")"]:

                #constraints
                if choice == "(" and open_count == n:
                    continue
                
                if choice == ")" and close_count == open_count:
                    continue

                
                curr.append(choice)

                if choice == "(":
                    backtrack(open_count+1,close_count,curr)
                else:
                    backtrack(open_count,close_count+1,curr)

                curr.pop()
            # # choose "("
            # if open_count < n:
            #     curr.append("(")
            #     backtrack(open_count + 1,close_count,curr)
            #     curr.pop()

            # if close_count < open_count:
            #     curr.append(")")
            #     backtrack(open_count, close_count + 1, curr)
            #     curr.pop()
            

        backtrack(0,0,[])

        return ans
        