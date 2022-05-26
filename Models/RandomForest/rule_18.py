def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9986
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 73, Entropy: 0.9605
      if obj[0]<=155.759995:
         # Feature: SMA1, Instances: 60, Entropy: 0.9007
         if obj[4] == 'Buy':
            # Feature: RSI, Instances: 38, Entropy: 0.7897
            if obj[1] == 'Hold':
               # Feature: SMA2, Instances: 35, Entropy: 0.8224
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 20, Entropy: 0.8813
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 15, Entropy: 0.7219
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 22, Entropy: 0.994
            if obj[5] == 'Sell':
               # Feature: RSI, Instances: 14, Entropy: 1.0
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 14, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: MACD, Instances: 8, Entropy: 0.9544
               if obj[2] == 'Sell':
                  # Feature: RSI, Instances: 7, Entropy: 0.9852
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[0]>155.759995:
         # Feature: SMA2, Instances: 13, Entropy: 0.8905
         if obj[5] == 'Sell':
            # Feature: SMA1, Instances: 7, Entropy: 0.9852
            if obj[4] == 'Buy':
               # Feature: RSI, Instances: 4, Entropy: 1.0
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: RSI, Instances: 3, Entropy: 0.9183
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Buy':
            # Feature: MACD, Instances: 6, Entropy: 0.65
            if obj[2] == 'Sell':
               # Feature: RSI, Instances: 4, Entropy: 0.8113
               if obj[1] == 'Hold':
                  # Feature: SMA1, Instances: 4, Entropy: 0.8113
                  if obj[4] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Buy':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: Closing, Instances: 38, Entropy: 0.6292
      if obj[0]<=155.759995:
         # Feature: SMA1, Instances: 31, Entropy: 0.7088
         if obj[4] == 'Buy':
            # Feature: RSI, Instances: 19, Entropy: 0.4855
            if obj[1] == 'Hold':
               # Feature: MACD, Instances: 12, Entropy: 0.65
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 11, Entropy: 0.684
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[1] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: RSI, Instances: 12, Entropy: 0.9183
            if obj[1] == 'Hold':
               # Feature: SMA2, Instances: 8, Entropy: 0.9544
               if obj[5] == 'Sell':
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[1] == 'Sell':
               # Feature: SMA2, Instances: 4, Entropy: 0.8113
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[0]>155.759995:
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
