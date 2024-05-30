class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_count = {}
        result = []
        distinct_colors = 0

        for query in queries:
            ball, color = query

            if ball in ball_colors:
                prev_color = ball_colors[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    distinct_colors -= 1

            ball_colors[ball] = color
            color_count[color] = color_count.get(color, 0) + 1
            if color_count[color] == 1:
                distinct_colors += 1

            result.append(distinct_colors)

        return result
