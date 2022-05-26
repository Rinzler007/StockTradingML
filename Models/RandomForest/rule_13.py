def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9995
   if obj[3] == 'Sell':
      # Feature: RSI, Instances: 69, Entropy: 0.8865
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 65, Entropy: 0.9077
         if obj[0]>33.924:
            # Feature: SMA1, Instances: 53, Entropy: 0.8595
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 30, Entropy: 0.9481
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 16, Entropy: 0.9887
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 14, Entropy: 0.8631
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 23, Entropy: 0.6666
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 13, Entropy: 0.7793
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 10, Entropy: 0.469
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]<=33.924:
            # Feature: SMA1, Instances: 12, Entropy: 1.0
            if obj[4] == 'Sell':
               # Feature: MACD, Instances: 6, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Buy':
               # Feature: SMA2, Instances: 6, Entropy: 0.9183
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 2, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[1] == 'Buy':
         return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 40, Entropy: 0.669
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 24, Entropy: 0.8709
         if obj[0]>33.924:
            # Feature: SMA1, Instances: 14, Entropy: 1.0
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 9, Entropy: 0.7642
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 8, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[0]<=33.924:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: SMA1, Instances: 6, Entropy: 0.9183
      if obj[4] == 'Sell':
         # Feature: Closing, Instances: 5, Entropy: 0.971
         if obj[0]>33.924:
            # Feature: RSI, Instances: 3, Entropy: 0.9183
            if obj[1] == 'Buy':
               # Feature: MACD, Instances: 2, Entropy: 1.0
               if obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Hold':
               return 'No'
            else:
               return 'No'
         elif obj[0]<=33.924:
            # Feature: RSI, Instances: 2, Entropy: 1.0
            if obj[1] == 'Buy':
               return 'No'
            elif obj[1] == 'Hold':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      elif obj[4] == 'Buy':
         return 'No'
      else:
         return 'No'
   else:
      return 'No'
